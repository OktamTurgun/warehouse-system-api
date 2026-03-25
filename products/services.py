from .models import Warehouse, Product, ProductMaterial

def calculate_materials(products_data):
    # 1. Barcha warehouse ma'lumotlarini xotiraga olamiz (bazaga teginmaymiz)
    temp_warehouse = {}
    for w in Warehouse.objects.select_related('material').order_by('id'):
        temp_warehouse[w.id] = {
            'material_id': w.material.id,
            'material_name': w.material.name,
            'remainder': w.remainder,
            'price': w.price,
        }

    result = []

    # 2. Har bir mahsulot uchun hisoblash
    for item in products_data:
        product_code = item['product_code']
        product_qty = item['quantity']

        product = Product.objects.get(code=product_code)
        materials_needed = ProductMaterial.objects.filter(
            product=product
        ).select_related('material')

        product_materials = []

        # 3. Har bir xomashyo uchun
        for pm in materials_needed:
            needed = pm.quantity * product_qty  # Kerakli umumiy miqdor
            material_id = pm.material.id

            # 4. Partiyalarni ketma-ket tekshir (FIFO)
            for wid, wdata in temp_warehouse.items():
                if needed <= 0:
                    break
                if wdata['material_id'] != material_id:
                    continue
                if wdata['remainder'] <= 0:
                    continue

                take = min(needed, wdata['remainder'])
                product_materials.append({
                    'warehouse_id': wid,
                    'material_name': wdata['material_name'],
                    'qty': take,
                    'price': wdata['price'],
                })
                wdata['remainder'] -= take  # Faqat xotirada ayiramiz!
                needed -= take

            # 5. Yetishmovchilik bo'lsa null bilan ko'rsatamiz
            if needed > 0:
                product_materials.append({
                    'warehouse_id': None,
                    'material_name': pm.material.name,
                    'qty': needed,
                    'price': None,
                })

        result.append({
            'product_name': product.name,
            'product_qty': product_qty,
            'product_materials': product_materials,
        })

    return result

# temp_warehouse  → bazadan bir marta o'qib, xotirada saqlaymiz
# needed          → hali olishim kerak bo'lgan miqdor
# take            → bu partiyadan olaman (min - ikkinchisidan kichigini oladi)
# remainder -= take → FAQAT xotirada ayiramiz, bazaga yozmaymiz!
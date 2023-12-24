"""
Flask blueprint - Components View
"""

from flask import Blueprint, redirect, request, abort, render_template, url_for, flash
from flask.json import jsonify

from ..models.component import Component
from ..repository.componentRepository import ComponentRepository
from ..repository.categoryRepository import CategoryRepository
from ..repository.brandRepository import BrandRepository
from ..repository.storeRepository import StoreRepository
from ..repository.addressRepository import AddressRepository
from ..services.barcodeService import BarcodeService

components_blueprint = Blueprint("components", __name__)


@components_blueprint.route("/components", methods=["GET"])
def list_components():
    """
    List all components with details from related tables
    """
    components_data = ComponentRepository.get_all_components()
    components = [Component(**data) for data in components_data]
    return jsonify([component.as_dict() for component in components])


@components_blueprint.route("/components/details", methods=["GET"])
def list_components_with_details():
    """
    List all components with details from related tables
    """
    components_data = ComponentRepository.get_all_components_with_details()
    return jsonify(components_data)


@components_blueprint.route("/components/add", methods=["POST"])
def add_component_with_details():
    data = request.json

    # Check and add Category
    category_id = data.get('category_id')
    if not category_id:
        category_id = CategoryRepository.add_category(data['category_name'], data['category_description'])

    # Check and add Brand
    brand_id = data.get('brand_id')
    if not brand_id:
        brand_id = BrandRepository.add_brand(data['brand_name'], data['brand_description'])

    # Check and add Address
    address_id = data.get('address_id')
    if not address_id:
        address_id = AddressRepository.add_address(data['street'], data['city'], data['state'], data['zip_code'],
                                                   data['country'])

    # Check and add Store
    store_id = data.get('store_id')
    if not store_id:
        store_id = StoreRepository.add_store(data['store_name'], address_id, data['store_phone'], data['store_email'])

    component_name = data['name'].upper().replace(" ", "")[:10]

    barcode_list = [component_name, category_id, brand_id, address_id, store_id]
    barcode_string = '-'.join(map(str, barcode_list))
    BarcodeService.generate(barcode_string)

    # Add the Component
    component_id = ComponentRepository.add_component(
        name=data['name'],
        category_id=category_id,
        brand_id=brand_id,
        store_id=store_id,
        price=data['price'],
        description=data['description'],
        stock_quantity=data['stock_quantity'],
        barcode=barcode_string
    )

    return jsonify({'component_id': component_id}), 201


@components_blueprint.route("/decode-barcode", methods=["POST"])
def decode_barcode():
    data = request.json
    barcode_string = data.get('barcode_string')

    if not barcode_string:
        return jsonify({'message': 'Barcode string is required'}), 400

    barcode_data = BarcodeService.decode(barcode_string)

    all_components = ComponentRepository.get_all_components_with_details()
    matched_component = next((comp for comp in all_components if comp['barcode'] == barcode_data), None)

    if matched_component is None:
        return jsonify({'message': 'No component found with this barcode in the database'}), 404
    else:
        return jsonify(matched_component), 200

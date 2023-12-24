import React, {useState} from 'react';
import axios from 'axios';
import {ToastContainer, toast} from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';
import './SearchComponent.css';

function SearchComponent() {
    const [selectedFileName, setSelectedFileName] = useState('');
    const [componentData, setComponentData] = useState(null);
    const [selectedBarcode, setSelectedBarcode] = useState('');

    const handleFileChange = (event) => {
        if (event.target.files.length > 0) {
            setSelectedFileName(event.target.files[0].name);
        }
    };

    const handleSubmit = async (event) => {
        event.preventDefault();
        if (!selectedFileName) {
            toast.error('Please select a barcode image to upload');
            return;
        }

        try {
            const response = await axios.post('http://localhost:8080/decode-barcode', {
                barcode_string: selectedFileName
            });
            setComponentData(response.data);
            setSelectedBarcode(selectedFileName);
            toast.success('Barcode decoded successfully');
        } catch (error) {
            console.error('Error decoding barcode:', error);
            toast.error('Error decoding barcode');
        }
    };

    return (
        <div className="section-spacing">
            <h2>Search Component by Barcode</h2>
            <form onSubmit={handleSubmit} className="search-component">
                <input type="file" onChange={handleFileChange} accept="image/*"/>
                <button type="submit">Decode Barcode</button>
            </form>

            {selectedBarcode && (
                <div>
                    <h3>Barcode Image</h3>
                    <img src={`http://localhost:8080/static/images/${selectedBarcode}`}
                         alt={`http://localhost:8080/static/images/${selectedBarcode}`} className="barcode-image"/>
                </div>
            )}

            {componentData && (
                <div className="search-component-details">
                    <h3>Component Details</h3>
                    <p>Name: {componentData.component_name}</p>
                    <p>Price: {componentData.price}</p>
                    <p>Description: {componentData.component_description}</p>
                    <p>Stock Quantity: {componentData.stock_quantity}</p>
                    <p>Barcode: {componentData.barcode}</p>
                    <p>Category Name: {componentData.category_name}</p>
                    <p>Category Description: {componentData.category_description}</p>
                    <p>Brand Name: {componentData.brand_name}</p>
                    <p>Brand Description: {componentData.brand_description}</p>
                    <p>Store Name: {componentData.store_name}</p>
                    <p>Store Phone: {componentData.store_phone}</p>
                    <p>Store Email: {componentData.store_email}</p>
                    <p>Street: {componentData.street}</p>
                    <p>City: {componentData.city}</p>
                    <p>State: {componentData.state}</p>
                    <p>Zip Code: {componentData.zip_code}</p>
                    <p>Country: {componentData.country}</p>
                </div>
            )}

            <ToastContainer/>
        </div>
    );
}

export default SearchComponent;

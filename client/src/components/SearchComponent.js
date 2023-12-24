import React, {useState} from 'react';
import axios from 'axios';
import {ToastContainer, toast} from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';
import './SearchComponent.css';
import {Spinner} from "react-bootstrap";

function SearchComponent() {
    const [selectedFileName, setSelectedFileName] = useState('');
    const [componentData, setComponentData] = useState(null);
    const [selectedBarcode, setSelectedBarcode] = useState('');
    const [isLoading, setIsLoading] = useState(false);

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
        setIsLoading(true);

        try {
            const response = await axios.post('http://localhost:8080/decode-barcode', {
                barcode_string: selectedFileName
            });
            setComponentData(response.data);
            setSelectedBarcode(selectedFileName);
            setIsLoading(false);
            toast.success('Barcode decoded successfully');
        } catch (error) {
            setIsLoading(false);
            console.error('Error decoding barcode:', error);
            toast.error('Error decoding barcode');
        }
    };

    return (
        <div className="section-spacing">
            <div className="search-component">
                <h2>Search Component by Barcode</h2>
                <form onSubmit={handleSubmit}>
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

                <div>
                    <h3>Component Details</h3>
                </div>

                {isLoading && (
                    <Spinner animation="border" role="status">
                        <span className="sr-only">Loading...</span>
                    </Spinner>
                )}

                {componentData && (
                    <div className="search-component-details">
                        <div className="detail-column">
                            <p><span className="detail-label">Name:</span> {componentData.component_name}</p>
                            <p><span className="detail-label">Price:</span> {componentData.price}</p>
                            <p><span className="detail-label">Description:</span> {componentData.component_description}
                            </p>
                            <p><span className="detail-label">Stock Quantity:</span> {componentData.stock_quantity}</p>
                            <p><span className="detail-label">Category Name:</span> {componentData.category_name}</p>
                            <p><span
                                className="detail-label">Category Description:</span> {componentData.category_description}
                            </p>
                            <p><span className="detail-label">Brand Name:</span> {componentData.brand_name}</p>
                            <p><span
                                className="detail-label">Brand Description:</span> {componentData.brand_description}</p>
                        </div>

                        <div className="detail-column">
                            <p><span className="detail-label">Store Name:</span> {componentData.store_name}</p>
                            <p><span className="detail-label">Store Phone:</span> {componentData.store_phone}</p>
                            <p><span className="detail-label">Store Email:</span> {componentData.store_email}</p>
                            <p><span className="detail-label">Street:</span> {componentData.street}</p>
                            <p><span className="detail-label">City:</span> {componentData.city}</p>
                            <p><span className="detail-label">State:</span> {componentData.state}</p>
                            <p><span className="detail-label">Zip Code:</span> {componentData.zip_code}</p>
                            <p><span className="detail-label">Country:</span> {componentData.country}</p>
                        </div>
                    </div>
                )}

            </div>

            <ToastContainer/>
        </div>
    );
}

export default SearchComponent;

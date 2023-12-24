import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Spinner } from 'react-bootstrap';
import './AllComponents.css';

function AllComponents() {
    const [components, setComponents] = useState([]);
    const [selectedBarcode, setSelectedBarcode] = useState('');

    const [isLoading, setIsLoading] = useState(true); // Loading state

    useEffect(() => {
        axios.get('http://localhost:8080/components/details')
            .then(response => {
                setComponents(response.data);
                console.log(response.data[0])
                setIsLoading(false); // Set loading to false once data is loaded
            })
            .catch(error => {
                console.error('Error fetching data:', error);
                setIsLoading(false); // Also set loading to false in case of error
            });
    }, []);

    if (isLoading) {
        return (
            <div className="spinner-container">
                <Spinner animation="border" role="status">
                    <span className="sr-only">Loading...</span>
                </Spinner>
            </div>
        );
    }

    const handleComponentClick = (barcode) => {
        setSelectedBarcode(barcode);
    };

    return (
        <div className="section-spacing">
            <h2>All Computer Components</h2>
            <table className="all-components-table">
                <thead>
                <tr>
                    <th>Computer Component Name</th>
                    <th>Price</th>
                    <th>Description</th>
                    <th>Stock Quantity</th>
                    <th>Category Name</th>
                    <th>Category Description</th>
                    <th>Brand Name</th>
                    <th>Brand Description</th>
                    <th>Store Name</th>
                    <th>Store Phone</th>
                    <th>Store Email</th>
                    <th>Street</th>
                    <th>City</th>
                    <th>State</th>
                    <th>Zip Code</th>
                    <th>Country</th>
                </tr>
                </thead>
                <tbody>
                {components.map((component, index) => (
                    <tr key={index}>
                        <td style={{ cursor: 'pointer' }} onClick={() => handleComponentClick(component.barcode)}>
                            {component.component_name}
                        </td>
                        <td>{component.price}</td>
                        <td>{component.component_description}</td>
                        <td>{component.stock_quantity}</td>
                        <td>{component.category_name}</td>
                        <td>{component.category_description}</td>
                        <td>{component.brand_name}</td>
                        <td>{component.brand_description}</td>
                        <td>{component.store_name}</td>
                        <td>{component.store_phone}</td>
                        <td>{component.store_email}</td>
                        <td>{component.street}</td>
                        <td>{component.city}</td>
                        <td>{component.state}</td>
                        <td>{component.zip_code}</td>
                        <td>{component.country}</td>
                    </tr>
                ))}
                </tbody>
            </table>
            {selectedBarcode && (
                <div>
                    <h3>Barcode Image</h3>
                    <img src={`http://localhost:8080/static/images/${selectedBarcode}.png`} alt={`http://localhost:8080/static/images/${selectedBarcode}.png`} />
                </div>
            )}
        </div>
    );
}

export default AllComponents;

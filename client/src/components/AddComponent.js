import React, { useState } from 'react';
import axios from 'axios';
import { ToastContainer, toast } from 'react-toastify';
import './AddComponent.css';

function AddComponent() {
    const initialFormData = {
        name: '',
        price: '',
        description: '',
        stock_quantity: '',
        category_name: '',
        category_description: '',
        brand_name: '',
        brand_description: '',
        store_name: '',
        store_phone: '',
        store_email: '',
        street: '',
        city: '',
        state: '',
        zip_code: '',
        country: ''
    };

    const [formData, setFormData] = useState(initialFormData);
    const [errors, setErrors] = useState({});

    const validateForm = () => {
        let isValid = true;
        let errors = {};

        if (!formData.name) {
            isValid = false;
            errors.name = 'Component name is required';
        } else if (formData.name.length > 50) {
            isValid = false;
            errors.name = 'Component name must be less than 50 characters';
        }

        if (!formData.price) {
            isValid = false;
            errors.price = 'Price is required';
        } else if (isNaN(formData.price) || Number(formData.price) <= 0) {
            isValid = false;
            errors.price = 'Price must be a positive number';
        }

        if (formData.description && formData.description.length > 200) {
            isValid = false;
            errors.description = 'Description must be less than 200 characters';
        }

        if (formData.stock_quantity && (isNaN(formData.stock_quantity) || Number(formData.stock_quantity) < 0)) {
            isValid = false;
            errors.stock_quantity = 'Stock quantity must be a non-negative number';
        }

        if (formData.category_name && formData.category_name.length > 50) {
            isValid = false;
            errors.category_name = 'Category name must be less than 50 characters';
        }

        if (formData.brand_name && formData.brand_name.length > 50) {
            isValid = false;
            errors.brand_name = 'Brand name must be less than 50 characters';
        }

        if (formData.store_name && formData.store_name.length > 50) {
            isValid = false;
            errors.store_name = 'Store name must be less than 50 characters';
        }

        setErrors(errors);
        return isValid;
    };


    const handleChange = (event) => {
        setFormData({ ...formData, [event.target.name]: event.target.value });
    };

    const handleSubmit = (event) => {
        event.preventDefault();
        if (validateForm()) {
            axios.post('http://localhost:8080/components/add', formData)
                .then(response => {
                    console.log('Component added:', response.data);
                    toast.success('Component added successfully!');
                    setFormData(initialFormData);
                })
                .catch(error => {
                    console.error('Error adding component:', error);
                    toast.error('Error adding component!');
                });
        }
    };

    return (
        <div className="section-spacing">
            <h2>Add Component</h2>
            <form onSubmit={handleSubmit} className="add-component-form">
                {/* Component Name */}
                <div>
                    <label>Component Name:</label>
                    <input
                        type="text"
                        name="name"
                        value={formData.name}
                        onChange={handleChange}
                        placeholder="Component Name"
                    />
                    {errors.name && <div className="error">{errors.name}</div>}
                </div>

                {/* Price */}
                <div>
                    <label>Price:</label>
                    <input
                        type="number"
                        name="price"
                        value={formData.price}
                        onChange={handleChange}
                        placeholder="Price"
                    />
                    {errors.price && <div className="error">{errors.price}</div>}
                </div>

                {/* Description */}
                <div>
                    <label>Description:</label>
                    <textarea
                        name="description"
                        value={formData.description}
                        onChange={handleChange}
                        placeholder="Description"
                    />
                    {errors.description && <div className="error">{errors.description}</div>}
                </div>

                {/* Stock Quantity */}
                <div>
                    <label>Stock Quantity:</label>
                    <input
                        type="number"
                        name="stock_quantity"
                        value={formData.stock_quantity}
                        onChange={handleChange}
                        placeholder="Stock Quantity"
                    />
                    {errors.stock_quantity && <div className="error">{errors.stock_quantity}</div>}
                </div>

                {/* Category Name */}
                <div>
                    <label>Category Name:</label>
                    <input
                        type="text"
                        name="categoryName"
                        value={formData.category_name}
                        onChange={handleChange}
                        placeholder="Category Name"
                    />
                    {errors.category_name && <div className="error">{errors.category_name}</div>}
                </div>

                {/* Category Description */}
                <div>
                    <label>Category Description:</label>
                    <textarea
                        name="category_description"
                        value={formData.category_description}
                        onChange={handleChange}
                        placeholder="Category Description"
                    />
                    {errors.category_description && <div className="error">{errors.category_description}</div>}
                </div>

                {/* Brand Name */}
                <div>
                    <label>Brand Name:</label>
                    <input
                        type="text"
                        name="brand_name"
                        value={formData.brand_name}
                        onChange={handleChange}
                        placeholder="Brand Name"
                    />
                    {errors.brand_name && <div className="error">{errors.brand_name}</div>}
                </div>

                {/* Brand Description */}
                <div>
                    <label>Brand Description:</label>
                    <textarea
                        name="brand_description"
                        value={formData.brand_description}
                        onChange={handleChange}
                        placeholder="Brand Description"
                    />
                    {errors.brand_description && <div className="error">{errors.brand_description}</div>}
                </div>

                {/* Store Name */}
                <div>
                    <label>Store Name:</label>
                    <input
                        type="text"
                        name="store_name"
                        value={formData.store_name}
                        onChange={handleChange}
                        placeholder="Store Name"
                    />
                    {errors.store_name && <div className="error">{errors.store_name}</div>}
                </div>

                {/* Store Phone */}
                <div>
                    <label>Store Phone:</label>
                    <input
                        type="text"
                        name="store_phone"
                        value={formData.store_phone}
                        onChange={handleChange}
                        placeholder="Store Phone"
                    />
                    {errors.store_phone && <div className="error">{errors.store_phone}</div>}
                </div>

                {/* Store Email */}
                <div>
                    <label>Store Email:</label>
                    <input
                        type="email"
                        name="store_email"
                        value={formData.store_email}
                        onChange={handleChange}
                        placeholder="Store Email"
                    />
                    {errors.store_email && <div className="error">{errors.store_email}</div>}
                </div>

                {/* Address Fields */}
                <div>
                    <label>Street:</label>
                    <input
                        type="text"
                        name="street"
                        value={formData.street}
                        onChange={handleChange}
                        placeholder="Street"
                    />
                    {errors.street && <div className="error">{errors.street}</div>}
                </div>

                <div>
                    <label>City:</label>
                    <input
                        type="text"
                        name="city"
                        value={formData.city}
                        onChange={handleChange}
                        placeholder="City"
                    />
                    {errors.city && <div className="error">{errors.city}</div>}
                </div>

                <div>
                    <label>State:</label>
                    <input
                        type="text"
                        name="state"
                        value={formData.state}
                        onChange={handleChange}
                        placeholder="State"
                    />
                    {errors.state && <div className="error">{errors.state}</div>}
                </div>

                <div>
                    <label>Zip Code:</label>
                    <input
                        type="text"
                        name="zip_code"
                        value={formData.zip_code}
                        onChange={handleChange}
                        placeholder="Zip Code"
                    />
                    {errors.zip_code && <div className="error">{errors.zip_code}</div>}
                </div>

                <div>
                    <label>Country:</label>
                    <input
                        type="text"
                        name="country"
                        value={formData.country}
                        onChange={handleChange}
                        placeholder="Country"
                    />
                    {errors.country && <div className="error">{errors.country}</div>}
                </div>

                <button type="submit">Add Component</button>
            </form>

            <ToastContainer/>
        </div>
    );

}

export default AddComponent;

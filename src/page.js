"use client"
import React, { useState } from 'react';
import styles from './page.module.css';
import axios from 'axios';
import { ResultsPopup } from './benefit-results';

export default function Home() {
    const [file, setFile] = useState(null);
    const [benefits, setBenefits] = useState([]);

    const handleFileChange = async (e) => {
        console.log('this is the file');
        const file = e.target.files[0];
        if (file) {
            
            setFile(file);

            const formData = new FormData();
            formData.append('file', file);

            try {
                const response = await axios.post('/api/parse', formData, {
                    headers: {
                        'Content-Type': 'multipart/form-data'
                    }
                });
                

                console.log('this is the response', response)


                // Now you can process the extractedText further...
                // For demonstration, let's assume you set it directly to benefits
                // setBenefits([extractedText]);
            } catch (error) {
                console.error("Error uploading and parsing the file:", error);
            }
        }
    };

    return (
        <><div className={styles.container}>
            <h1 className={styles.header}>PDF Benefits Analyzer</h1>
            <h2 className={styles.subHeader}>Upload a copy of your employment agreement and discover your benefits within seconds!</h2>

            <input
                type="file"
                accept=".pdf"
                onChange={(e) => {handleFileChange(e)}}
                className={styles.uploadButton}
            />
            
            <div className={styles.resultsSection}>
                {benefits.map((benefit, index) => (
                    <p key={index}>{benefit}</p>
                ))}
            </div>

        </div>
        <ResultsPopup /></>
    );
}

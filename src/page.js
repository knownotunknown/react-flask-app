"use client"
import React, { useState } from 'react';
import styles from './page.module.css';
import { ResultsPopup } from './benefit-results';

export default function Home() {
    const [file, setFile] = useState(null);
    const [benefits, setBenefits] = useState([]);

    const handleFileChange = (e) => {
        const file = e.target.files[0];
        if (file) {
            setFile(file);
        }
    };

    return (
        <>
        <div className={styles.container}>
            <h1 className={styles.header}>PDF Benefits Analyzer</h1>
            <h2 className={styles.subHeader}>Upload a copy of your employment agreement and discover your benefits within seconds!</h2>

            <input
                type="file"
                accept=".pdf"
                onChange={handleFileChange}
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

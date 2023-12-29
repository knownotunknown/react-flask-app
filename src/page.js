"use client"
import React, { useState } from 'react';
import styles from './page.module.css';
import axios from 'axios';
import CircularProgress from '@mui/material/CircularProgress';
import Box from '@mui/material/Box';
import InfoOutlinedIcon from '@mui/icons-material/InfoOutlined';
import { ResultsPopup } from './benefit-results';
import Dialog from '@mui/material/Dialog';
import DialogTitle from '@mui/material/DialogTitle';

export default function Home() {
    const [benefits, setBenefits] = useState(null);
    const [isLoading, setIsLoading] = useState(false);
    const [openChallengeDetails, setOpenChallengeDetails] = useState(false);


    const handleFileChange = async (e) => {
        console.log('this is the file');
        const file = e.target.files[0];
        if (file) {
            setIsLoading(true);

            const formData = new FormData();
            formData.append('file', file);

            try {
                const response = await axios.post('/upload_doc', formData, {
                    headers: {
                        'Content-Type': 'multipart/form-data'
                    }
                });
                

                console.log('this is the response', response.data)
                setBenefits(response.data);

            } catch (error) {
                console.error("Error uploading and parsing the file:", error);
            } finally {
                setIsLoading(false); 
            }
        }
    };

    return (
        <>
        <InfoOutlinedIcon onClick = {() => {setOpenChallengeDetails(true)}} style={{
        position: 'absolute',
        top: 10,
        left: 10,
        cursor: 'pointer'
        }} />
        <Dialog onClose={() => {setOpenChallengeDetails(false)}} open={openChallengeDetails} style={{ width: '100%', maxWidth: '600px', margin: 'auto' }}>
            <DialogTitle style={{ fontWeight: 'bold' }}>Challenge:</DialogTitle>
            <p style={{ margin: '20px 20px', textAlign: 'justify' }}>
            In the current job market, worker benefits are often extremely difficult to track--from difficult language in insurance 
            contracts to hard-to-decipher instructions from HR. Propose easy-to-use tools that are able to reduce the friction of 
            employees attempting to understand how much of their benefits they are missing out on. Do so in a way such that employee 
            personal information remains private.
            </p>
            <DialogTitle style={{ fontWeight: 'bold' }}>Solution:</DialogTitle>
            <p style={{ margin: '20px 20px', textAlign: 'justify' }}>
            Our pdf analyzer identifies what benefits employees are entitled to with AI. We use semantic search to identify what sentences
            are closest to a predefined list of common benefits. We host the SBERT pre-trained model locally, so that employee data remains secure
            (compared to making an API call to ChatGPT).
            </p>
        </Dialog>
        <div className={styles.container}>
            <h1 className={styles.header}>PDF Benefits Analyzer</h1>
            <h2 className={styles.subHeader}>Upload a copy of your employment agreement and discover your benefits within seconds!</h2>

            <input
                type="file"
                accept=".pdf"
                onChange={(e) => {handleFileChange(e)}}
                className={styles.uploadButton}
            />

            {isLoading && (
                <Box sx={{ position: 'fixed', top: '50%', left: '50%', transform: 'translate(-50%, -50%)'}}>
                    <CircularIndeterminate />
                </Box>
            )}
        </div>

        <ResultsPopup keywords_to_exact_text = {benefits}/></>
        
    );
}

function CircularIndeterminate() {
  return (
    <Box sx={{ display: 'flex' }}>
      <CircularProgress />
    </Box>
  );
}

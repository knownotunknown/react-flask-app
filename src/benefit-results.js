"use client" 
//import OpenAi from 'openai-api';
import React, { useState } from 'react';
import styles from './results.module.css';
//import { Checkmark } from 'react-checkmark';
import CheckCircleIcon from '@mui/icons-material/CheckCircle';

const openAIKey = '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';
//const openai = new OpenAI();

const COLOR_GREEN = "success";
const COLOR_GRAY = "primary";

export function ResultsPopup(/**/) {
  const [keywords, setKeywords] = useState([
    'free gym membership', 'development', 'python', 'business analysis',
    'capital markets'
  ]);
  const [exactTexts, setExactTests] = useState(Array(keywords.length).fill('NULL'));

  const [checkmarkColors, setCheckmarkColors] = useState(Array(keywords.length).fill(COLOR_GREEN));
  
  const handleChatGPTCall = (keyword) => {
    const messages = [{"role": "user", "content": 
    `Can you explain the following employee benefit to me, an ignorant employee: ${keyword}?`}];
  }

  return (
    <div className={styles.resultsPopup}>
      <h3>Matches found...</h3>
      <ul>
        {keywords.map((keyword, index) => { 
        return <div className = {styles.entry}>
        <CheckCircleIcon fontSize = 'large' color={checkmarkColors[index] || COLOR_GREEN}/>
        <li key={index} onClick={handleChatGPTCall(exactTexts[index])}>{keyword}</li>
        </div>
        }
        )}
      </ul>
    </div>
  );
}


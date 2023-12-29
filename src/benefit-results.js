"use client" 
import React, { useState } from 'react';
import styles from './results.module.css';
import CheckCircleIcon from '@mui/icons-material/CheckCircle';
import Dialog from '@mui/material/Dialog';
import List from '@mui/material/List';
import ListItem from '@mui/material/ListItem';
import ListItemText from '@mui/material/ListItemText';
import DialogTitle from '@mui/material/DialogTitle';

const openAIKey = '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';
//const openai = new OpenAI();

const COLOR_GREEN = "success";
const COLOR_GRAY = "primary";

export function ResultsPopup(props) {
  /*const [keywords2, setKeywords2] = useState([
    'free gym membership', 'development', 'python', 'business analysis',
    'capital markets'
  ]);*/
  let size = props.keywords_to_exact_text ? props.keywords_to_exact_text.length : 0;
  
  const [exactTexts, setExactTests] = useState([]);
  const [checkmarkColors, setCheckmarkColors] = useState(Array(size).fill(COLOR_GREEN));
  const [open, setOpen] = useState(false);
  const [dialogOpen, setDialogOpen] = useState(false);

  if (props.keywords_to_exact_text == null) {
    console.log(props);
    return null;
  }

  const keywords = Object.keys(props.keywords_to_exact_text);

  const handlePopup = (sentences) => {
    setExactTests(sentences);
    setDialogOpen(true);
  }
  console.log('this is the keyword_to_exact_text', props.keywords_to_exact_text);

  return (
    <>
      <div className={styles.resultsPopup}>
        <h3>Matches found...</h3>
        <ul>
          {keywords.map((keyword, index) => { 
          return <div style={{ cursor: 'pointer' }} className = {styles.entry} onClick={() => handlePopup(props.keywords_to_exact_text[keyword])}>
          <CheckCircleIcon fontSize = 'large' color={checkmarkColors[index] || COLOR_GREEN}/>
          <li  key={index}>{keyword}</li>
          </div>
          }
          )}
        </ul>
      </div>
      <Dialog onClose={() => {setDialogOpen(false)}} open={dialogOpen}>
        <DialogTitle>Exact sentences from offer letter</DialogTitle>
          <List sx={{ pt: 0 }}>
            {exactTexts.map((text) => (
              <ListItem key={text}>
                  <ListItemText primary={text} />
              </ListItem>
            ))}
            </List>
        </Dialog>
    </>
  );
}


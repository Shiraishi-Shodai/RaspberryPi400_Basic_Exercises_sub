import React from 'react'
import axios from "axios";
import * as setting from '../setting.js';

function Streaming() {

    const recoding_start = () => {
        const rec_start = async() => {
          axios.get('/recoding')
          .then(response => {
            console.log(response.data); // レスポンスデータ
            console.log(response.status); // 200
            console.log(response.statusText); // 'OK'
            // ...
          });
        }
    
        rec_start();
      }
      
  return (
    <div>

        <img src="http://localhost:5000/video_feed" alt="video feed" />
        <button type='button' onClick={recoding_start}>録画開始</button>
        <button type='button'>録画停止</button>

    </div>
  )
}

export default Streaming
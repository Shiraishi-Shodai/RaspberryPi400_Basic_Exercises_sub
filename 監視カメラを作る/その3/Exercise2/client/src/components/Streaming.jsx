import React from 'react'
import axios from "axios";
// import * as setting from '../setting.js';

function Streaming() {

      const instance = axios.create({
        baseURL: 'http://localhost:5000',
        headers: {
          'Content-Type': 'application/json',
          'Access-Control-Allow-Origin': '*',
          'Access-Control-Allow-Headers': '*',
        }
      });

      const recoding_start = async() => {
        instance.get('/recoding')
        .then(response => {
          console.log(response.data); // レスポンスデータ
          console.log(response.status); // 200
          console.log(response.statusText); // 'OK'
          console.log(response.config); // 'OK'
          // ...
        }).catch(
          error => {console.log(error.response);}
        );
      }
          
      const recoding_stop = async() => {
        instance.post('/recoding', {"message": "録画を停止してください"})
        .then((response) => { 
          console.log(response.data);//レスポンスデータ
          console.log(response.status); // 200
          console.log(response.statusText); // 'OK'
          // ...
        }).catch(
          error => {console.log(error.response);}
        );
;
      }
              
  return (
    <div>

        <img src="http://localhost:5000/video_feed" alt="video feed" />
        <button type='button' onClick={recoding_start}>録画開始</button>
        <button type='button' onClick={recoding_stop}>録画停止</button>

    </div>
  )
}

export default Streaming
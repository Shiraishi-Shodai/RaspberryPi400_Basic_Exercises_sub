import React, { useState } from 'react'
import axios from "axios";
import * as setting from '../setting.js';
import {Route, Routes, Link } from 'react-router-dom'
import './Streaming.css'

function Streaming({setModal}) {

      const [disable, setDisable] = useState(true);

      const recoding_start = async() => {

        setDisable(!disable); //録画開始ボタンが押されたらdisableの値を変換する
        axios.get('/recoding')
        .then(response => {
          console.log("streaming - get" + response.data); // レスポンスデータ
          // ...
        }).catch(
          error => {console.log(error.response);}
        );
      }
               
      const recoding_stop = async() => {
        setModal(true);
        axios.post('/recoding', {"message": "録画を停止してください"})
        .then((response) => { 
          console.log("streaming - post" + response.data);//レスポンスデータ
          // ...
        }).catch(
          error => {console.log(error.response);}
        );
      }

  return (
    <div className='container'>
      <div className="child">

        <img src="http://localhost:5000/video_feed" alt="video feed" />
        <div className='buttons'>

          <button type='button' disabled={!disable} onClick={recoding_start} className='start'>録画開始</button>        
          <Link to='/modal'><button type='button' disabled={disable} onClick={recoding_stop} className='stop'>録画停止</button></Link>
          
        </div>
      </div>

    </div>
  )
}

export default Streaming
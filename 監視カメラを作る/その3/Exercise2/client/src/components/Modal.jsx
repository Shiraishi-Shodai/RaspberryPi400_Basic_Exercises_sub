import React, { useState } from 'react'
import axios from "axios";
import './Modal.css';
import * as setting from '../setting.js';
import { Link } from 'react-router-dom';

function Modal({modal}) {
    const [fileNme, setFileName] = useState(''); 

    const handleFileName = (e)=> {
        let text = e.target.value;
        if(text.trim() !== "") {
            setFileName(e.target.value);
        }
    }

    const sendFileName = async()=> {
        axios.post('/save', {'fileName': fileNme})
        .then((res) => {
            console.log(res.data);
            console.log(res.status);
            alert(res.data);
        }).catch((res)=> {
            console.log("modal" + res.response);
        })
    }

    return modal ? (
        <div id="overlay">
          <div id="content">
            <p>ファイル名を入力してください。保存先に同じ名前を持つファイルが存在する場合は上書きされます</p>
            <label htmlFor="file_name">
                <input type="text" name="file_name" id="file_name" onChange={handleFileName}/>
            </label>
            {/* <Link to="/"> */}
            <button onClick={sendFileName}>決定</button>
            {/* </Link> */}
          </div>
        </div>
      ) : null;
}

export default Modal
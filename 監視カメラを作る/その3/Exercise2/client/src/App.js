import './App.css';
import React, {useState} from 'react';
import Streaming from './components/Streaming.jsx';
import {Route, Routes} from 'react-router-dom'
import Modal from './components/Modal.jsx';

function App() {

    const [modal, setModal] = useState(false);
    return (
        <div className="App">

          <Routes>
            <Route path='/' element={<Streaming setModal={setModal}/>}></Route>
            <Route path='/modal' element={<Modal modal={modal}/>}></Route>
          </Routes>

        </div>
    );
}

export default App;

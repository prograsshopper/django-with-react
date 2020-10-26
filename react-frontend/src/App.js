import React from 'react';
import 'App.css';
import { Button } from 'antd';




function App() {
  return (
    <div>
        <button>
        Hello react
        </button>

        <Button type="primary" onClick={ () => console.log("clicked") }>
            Hello Antd
        </Button>
    </div>
  );
}

export default App;

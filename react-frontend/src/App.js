import React from 'react';
import 'App.css';
import { Button } from 'antd';


const actions = {
    init(initialValue) {
        return { value: initialValue }
    },
    increment(prevState){
        return {value: prevState.value + 1};
    }, 
    decrement(prevState){
        return {value: prevState.value - 1};
    }
}

class Counter1 extends React.Component {
    state = actions.init(this.props.initialValue);
    // constructor(props) {
    //     super(props);
    //     this.state = actions.init(this.props.initialValue);
    // }

    onClick = () => {
        // this.setState({value: this.state.value + 1});
        // this.setState({value: this.state.value + 1});
         

        this.setState((prevState) => {
            const { value } = prevState;
            return { value: value + 1};
        });

        this.setState((prevState) => {
            const { value } = prevState;
            return { value: value + 1};
        });
        
    };

    render() {
        const { value } = this.state;
        return (
            <div>
                Counter1: {value}
                <Button onClick={() => this.setState(actions.increment)}>+1</Button>
                <Button onClick={() => this.setState(actions.decrement)}>-1</Button>
            </div>
        ); 
    }
}


function App() {

  return (
    <div>
        <div>
            <Counter1 initialValue={10} />
        </div> 
    </div>
  );
}

export default App;

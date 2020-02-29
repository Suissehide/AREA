import React from 'react';
import '../css/index.css';

import Drop from "../components/Drop";

class Notfound extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            start: false,
            drops: [
                { id: 1, type: 'coin', x: '10', y: '10' },
            ],
            playerX: 50,
            update: true,
            id: 0,
        };

        document.addEventListener('keydown', this.handleKeyDown);
    }

    componentDidMount() {
        this.timerID = setInterval(
            () => this.tick(),
            100
        );
    }

    componentWillUnmount() {
        clearInterval(this.timerID);
    }

    tick = () => {
        if (!this.state.start)
            return;
        this.update();
    };

    handleKeyDown = (event) => {
        event.preventDefault();

        if (event.key === 'q' && this.state.playerX > 0 && this.state.start)
            this.setState({ playerX: this.state.playerX - 3 });
        if (event.key === 'd' && this.state.playerX < 93 && this.state.start)
            this.setState({ playerX: this.state.playerX + 3 });
        console.log(this.state.playerX);
    };


    update = () => {
        const rand = Math.random() * 100;
        if (rand > 95) {
            this.setState(previousState => ({
                drops: [...previousState.drops, { type: 'coin', x: Math.random() * window.innerWidth, y: '10' }],
            }));
        }
        this.state.drops.map((drop) => {
            return (
               drop.y = parseInt(drop.y) + 10
            );
        });
        this.remove();
        this.setState({ update: !this.state.update });
    };

    remove = () => {
        this.setState({
            drops: this.state.drops.filter(function (drop) {
                return parseInt(drop.y) + 95 < window.innerHeight
            })
        });
    };

    render() {
        const drops = this.state.drops.map(function (drop, i) {
            return <Drop key={i} x={drop.x} y={drop.y} />;
        });

        if (!this.state.start)
            return (
                <div className="container-404">
                    <div>All we have here is...</div>
                    <h1>404</h1>
                    <div>
                        <button>Go back down</button>
                        <button onClick={() => this.setState({ start: true })} className="start-button">Or hit start</button>
                    </div>
                </div>
            );
        else
            return (
                <div className="container-404">
                    <div className="drop-container">
                        <ul>
                            {drops}
                        </ul>
                    </div>
                    <div className="player" style={{ left: this.state.playerX + '%' }} />
                </div>
            );
    }
}

export default Notfound

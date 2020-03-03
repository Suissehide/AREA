import React from 'react';
import config from '../../../services/Config';

class TopMangaWidget extends React.Component {

    state = {
        pos: 0,
        data: null,
    };

    componentDidMount() {
        this._fetch();
    }

    _fetch = () => {
        const url = `${config.serverIp}/api/jikan/top_manga`;

        fetch(url, {
            method: "GET",
            headers: {},
        })
            .then(response => response.json())
            .then(responseJson => {
                this.setState({ data: responseJson.top });
            })
            .catch(error => {
                console.error('Error: ', error);
            })
    };

    _incPos = () => {
        this.setState({ pos: this.state.pos >= this.state.data.length - 1 ? this.state.data.length - 1 : this.state.pos + 1 })
    };

    _decPos = () => {
        this.setState({ pos: this.state.pos > 0 ? this.state.pos - 1 : 0 })
    };

    render() {
        if (typeof (this.state.data) !== 'undefined' && this.state.data) {
            const d = this.state.data[this.state.pos];
            return (
                <>
                    <div className="flex flex-space-between flex-align-items">
                        <button className="submit chevron" onClick={this._decPos}><i className="fas fa-chevron-left" /></button>
                        <div className="flex flex-align-items flex-space-between flex-100">
                            <div><div className="rank">{d.rank}</div></div>
                            <div><img className="picture" src={d.imageUrl} alt="" /></div>
                            <div className="manga-content">
                                <p className="manga-title">{d.title}</p>
                                <p>{d.type}</p>
                                <p>{d.startDate}</p>
                            </div>
                            <div className="score"><i className="fas fa-star" /> {d.score}</div>
                        </div>
                        <button className="submit chevron" onClick={this._incPos}><i className="fas fa-chevron-right" /></button>
                    </div>
                </>
            );
        } else {
            return (
                <div />
            )
        }
    }
}

export default TopMangaWidget

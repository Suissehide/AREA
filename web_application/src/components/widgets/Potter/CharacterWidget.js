import React from 'react';
import config from '../../../services/Config';

class CharacterWidget extends React.Component {

    state = {
        data: [],
    };

    componentDidMount() {
        this._fetch();
    }

    _handleRefresh = () => {
        this._fetch();
    };

    _fetch = () => {
        const url = `${config.serverIp}/api/potter/character`;

        fetch(url, {
            method: "GET",
            headers: {},
        })
            .then(response => response.json())
            .then(responseJson => {
                this.setState({ data: responseJson });
            })
            .catch(error => {
                console.error('Error: ', error);
            })
    };

    render() {
        if (this.state.data) {
            const d = this.state.data;
            return (
                <>
                    <div>
                        <h1> {d.name} </h1>
                        {d.role !== null ? <em>{d.role}</em> : null}
                        <p>This Character is a {d.species} and its blood status is {d.bloodStatus}.</p>
                        {d.school !== null ? <p> {d.name} went to {d.school}</p> : null}
                        {d.house !== null ? <p>and more precisely in {d.house} house.</p> : d.house}
                        {d.ministryOfMagic === false && d.orderOfThePhoenix === false && d.dumbledoresArmy === false && d.deathEater === false ? <p>{d.name} doesn{"'"}t have any affiliation.</p> : <p>{d.name} {"'"}s affiliations are :</p>}
                        {d.ministryOfMagic !== false ? <p>{'['}Ministry of Magic{']'}</p> : null}
                        {d.orderOfThePhoenix !== false ? <p>{'['}Order Of The Phoenix{']'}</p> : null}
                        {d.dumbledoresArmy !== false ? <p>{'['}Dumbledore{"'"}s Army{']'}</p> : null}
                        {d.deathEater !== false ? <p>{'['}Death Eater{']'}</p> : null}
                    </div>
                    <button type="button" className="submit refresh" onClick={this._handleRefresh}><i className="fa fa-sync" /></button>
                </>
            );
        } else {
            return (
                <>
                    <button type="button" className="submit refresh" onClick={this._handleRefresh}><i className="fa fa-sync" /></button>
                </>
            )
        }
    }
}

export default CharacterWidget

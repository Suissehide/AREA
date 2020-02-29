import React from 'react';
import qs from 'query-string';

class Microsoft extends React.Component {
    state = {};

    componentDidMount() {
        const token = qs.parse(this.props.location.hash, { ignoreQueryPrefix: true }).access_token;
        this._getJeton(token);
    }

    _getJeton = async (token) => {
        if (!token)
            return;

        const url = `https://login.microsoftonline.com/901cb4ca-b862-4029-9306-e5cd0f6d9f86/oauth2/v2.0/token`;

        console.log(token);

        await fetch(url, {
            method: "POST",
            headers: {
                // 'Access-Control-Allow-Origin': '*',
                // 'Access-Control-Allow-Headers': 'Origin, Content-Type, Accept, X-Auth-Token',
                // 'Access-Control-Allow-Credentials': 'true',
                // 'Access-Control-Request-Headers': 'Origin, X-Custom-Header, X-Requested-With, Authorization, Content-Type, Accept',
                // 'Access-Control-Expose-Headers': 'Content-Length, X-Kuma-Revision',
                // 'Access-Control-Allow-Methods': 'GET, POST, PUT, DELETE, PATCH, OPTIONS',
                'Content-Type': 'application/x-www-form-urlencoded',
            },
            body: {
                'client_id': '04bd8816-75eb-4996-b663-fdce462165d1',
                'client_secret': '=h]2z.el1a79OYfarQD/aodAmmRkk=5T',
                'redirect_uri': 'http://localhost:3000/microsoft',
                'grant_type': 'authorization_code',
                'code': token,
                'scope': 'openid+Mail.Read',
            },
        })
            .then(response => {
                console.log(response)
            })
            .then(responseJson => {
                console.log(responseJson);
            })
            .catch(error => {
                this.setState({error, loading: false});
                console.error('Error: ', error);
            })
    };

    render() {
        const url = 'https://login.microsoftonline.com/901cb4ca-b862-4029-9306-e5cd0f6d9f86/oauth2/v2.0/authorize?client_id=04bd8816-75eb-4996-b663-fdce462165d1&redirect_uri=http://localhost:3000/microsoft&response_type=token&scope=openid+Mail.Read';

        return (
            <div>
                {/*<button onClick={() => window.open(url, "_blank")} className="btn">Auth</button>*/}
                <a href={url} className="btn">Auth</a>
            </div>
        )
    }
}

export default Microsoft

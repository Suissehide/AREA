import React from 'react';

class Footer extends React.Component {
    render() {
        return (
            <footer className="footer">
                <div className="container-fluid footer__flex">
                    <nav>
                        <ul>
                            <li><a href="#0">About us</a></li>
                            <li><a href="#0">Blog</a></li>
                            <li><a href="#0">Licenses</a></li>
                        </ul>
                    </nav>
                    <div className="copyright">
                        @2020, made with <i className="fas fa-heart"/> by <a href="#0" target="_blank">Léo
                        Couffinhal</a>
                    </div>
                </div>
            </footer>
        )
    }
}

export default Footer;


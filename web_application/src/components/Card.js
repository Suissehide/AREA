import React from 'react';
import '../css/Card.css';

class Card extends React.Component {

    render() {
        return (
            <div className="card card-stats">
                <div className={"card-header card-header-icon " + this.props.type}>
                    <div className="card-icon">
                        <i className={this.props.headerIcon}/>
                    </div>
                    <p className="card-category">{this.props.category}</p>
                    <h3 className="card-title">{this.props.title}</h3>
                </div>
                <div className="card-footer">
                    <div className="stats">
                        <i className={this.props.footerIcon}/> {this.props.footerText}
                    </div>
                </div>
            </div>
        );
    }
}

export default Card

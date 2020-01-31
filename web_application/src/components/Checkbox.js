import React from "react";

class Checkbox extends React.Component {
    render() {
        return (
            <div className="login-form-checkbox">
                <input className="input-checkbox" id="ckb1" name="_remember_me" type="checkbox"/>
                <label className="label-checkbox" htmlFor="ckb1">
                    Remember me
                </label>
            </div>
        );
    }
}

export default Checkbox

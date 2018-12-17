
/* ================================================================================
 *    Import React
 * ================================================================================ */

import React from "react"


/* ================================================================================
 *    Define Component
 * ================================================================================ */

export default class KeystrokeButton extends React.Component {

  constructor() {
    super()
  }

  render() {
    return (
      <div className="submit-btn">
        <input id="cancelBtn" type="button" value="Cancel" onClick={this.props.resetStroke} />
        <input id="okBtn" type="button" value={this.props.btnValue} onClick={this.props.nextStroke} />
      </div>
    )
  }

}
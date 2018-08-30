
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
    this._nextStroke  = this._nextStroke.bind(this)
    this._resetStroke = this._resetStroke.bind(this)
  }

  _nextStroke() {
    this.props.nextStroke()
  }

  _resetStroke() {
    this.props.resetStroke()
  }

  render() {
    return (
      <div className="submit-btn">
        <input id="cancelBtn" type="button" value="Cancel" onClick={this._resetStroke} />
        <input id="okBtn" type="button" value={this.props.btnValue} onClick={this._nextStroke} />
      </div>
    )
  }

}
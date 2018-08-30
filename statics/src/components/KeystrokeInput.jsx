
/* ================================================================================
 *    Import React
 * ================================================================================ */

import React from "react"


/* ================================================================================
 *    Define Component
 * ================================================================================ */

export default class KeystrokeInput extends React.Component {

  constructor() {
    super()
    this._onStroke = this._onStroke.bind(this)
  }

  _onStroke(e) {
    let key  = this.getKey(e.keyCode)
    let event = e.type == "keydown" ? "p" : "r"
    let time = this.getDate(new Date())

    if(key)
      this.props.onStroke({ key: key, event: event, time: time })
  }

  getKey(c) {
    if(c >= 65 && c <= 90)
      return String.fromCharCode(c).toLowerCase()
    else
      return undefined
  }

  getDate(date) {
    return date.getTime()
  }

  clearForm() {
    document.getElementById("keyForm").value = ""
  }

  focusForm() {
    document.getElementById("keyForm").focus()
  }

  render() {
    return (
      <div className="input-box">
        <input id="keyForm" type="text" name="keyForm" onKeyDown={this._onStroke} onKeyUp={this._onStroke} />
      </div>
    )
  }

}

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
    let key  = this.getKey(e.keyCode, e.shiftKey)
    let event = e.type == "keydown" ? "p" : "r"
    let time = this.getDate(new Date()) / 1000

    this.props.onStroke({ key: key, event: event, time: time })
  }

  getKey(c, shift) {
    const spkeyList = { 8: "Backspace", 13: "Enter", 16: "Shift", 17: "Ctrl", 18: "Alt", 20: "CapsLock" }

    if(c in spkeyList)
      return spkeyList[c]
    if(shift)
      return String.fromCharCode(c)
    return String.fromCharCode(c).toLowerCase()
  }

  getDate(date) {
    return date.getTime()
  }

  clearForm() {
    document.getElementById("keyForm").value = ""
  }

  render() {
    return (
      <div className="input-box">
        <input id="keyForm" type="text" name="keyForm" onKeyDown={this._onStroke} onKeyUp={this._onStroke} />
      </div>
    )
  }

}

/* ================================================================================
 *    Import React
 * ================================================================================ */

import React from "react"
import axios from "axios"


/* ================================================================================
 *    Import Component
 * ================================================================================ */

import KeystrokeInput   from "./KeystrokeInput"
import KeystrokeButton  from "./KeystrokeButton"


/* ================================================================================
 *    Define Component
 * ================================================================================ */

export default class Keystroke extends React.Component {

  constructor() {
    super();
    this.state       = { strokesList: [], strokes: [], count: 1, btnValue: "OK" }
    this.onStroke    = this.onStroke.bind(this)
    this.saveStroke  = this.saveStroke.bind(this)
    this.resetStroke = this.resetStroke.bind(this)
    this.nextStroke  = this.nextStroke.bind(this)
    this.countCheck  = this.countCheck.bind(this)
  }

  componentDidMount() {
    this.refs.KeystrokeInput.focusForm()
  }

  onStroke(newStroke) {
    this.state.strokes.push(newStroke)
    this.setState({ strokes: this.state.strokes })
  }

  saveStroke() {
    axios.post("/register", { "strokesList": this.state.strokesList} ).then(resp => {
      location.href = "/"
    }).catch(error => {
      console.log(error)
    })
  }

  resetStroke() {
    this.setState({ strokes: [] })
    this.refs.KeystrokeInput.clearForm()
    this.refs.KeystrokeInput.focusForm()
  }

  nextStroke() {
    let sentence = ""
    this.state.strokes.forEach(stroke => {
      if(stroke["event"] == "p")
        sentence += stroke["key"]
    })
    if(sentence != "inumoarukebabouniataru") {
      this.resetStroke()
      return
    }

    if(this.state.strokes[0]["key"] == "r" && this.state.strokes[0]["event"] == "r")
      this.state.strokes.splice(0, 1)

    let newList = []
    let tmpList = []
    this.state.strokes.forEach(stroke => {
      if(stroke["event"] == "p") {
        newList.push({ "key": stroke["key"], "press": stroke["time"], "release": "" })
        tmpList.push({ "key": stroke["key"], "index": newList.length - 1})
      } else {
        let target = tmpList.find(v => v["key"] == stroke["key"])
        tmpList.splice(tmpList.indexOf(target), 1)
        newList[target["index"]]["release"] = stroke["time"]
      }
    })

    this.state.strokesList.push(newList)
    this.setState({ strokesList: this.state.strokesList })
    this.resetStroke()
    this.countCheck()
  }

  countCheck() {
    if(this.state.count < 12) {
      this.setState({ count: this.state.count + 1 })
      if(this.state.count == 11)
        this.setState({ btnValue: "Finish" })
    } else
      this.saveStroke()
  }

  render() {
    return (
      <div className="wrap">
        <KeystrokeInput ref="KeystrokeInput" onStroke={this.onStroke} />
        <div className="counter">{ this.state.count } / 12</div>
        <KeystrokeButton ref="KeystrokeButton" resetStroke={this.resetStroke} nextStroke={this.nextStroke} btnValue={this.state.btnValue} />
      </div>
    )
  }

}

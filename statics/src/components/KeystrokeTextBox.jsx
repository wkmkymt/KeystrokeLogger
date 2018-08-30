
/* ================================================================================
 *    Import React
 * ================================================================================ */

import React from "react"


/* ================================================================================
 *    Define Component
 * ================================================================================ */

export default class KeystrokeTextBox extends React.Component {

  constructor() {
    super()
  }

  render() {
    return (
      <div id="textarea">
        <span>わたしは[FIRST][LAST]といいます</span><br/>
        WATASHI HA [FIRST] [LAST] TO IIMASU
      </div>
    )
  }

}
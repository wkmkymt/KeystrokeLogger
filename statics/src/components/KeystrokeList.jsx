
/* ================================================================================
 *    Import React
 * ================================================================================ */

import React from "react"


/* ================================================================================
 *    Define Component
 * ================================================================================ */

export default class KeystrokeList extends React.Component {

  constructor() {
    super()
  }

  render() {
    return (
      <table className="keystrokeList">
        <thead>
          <tr>
            <th>Key</th>
            <th>Event</th>
            <th>Time</th>
          </tr>
        </thead>
        <tbody>
        {
          this.props.strokes.map((stroke, index) => {
            return (
              <tr key={index}>
                <td>{ stroke.key }</td>
                <td>{ stroke.event }</td>
                <td>{ stroke.time }</td>
              </tr>
            )
          })
        }
        </tbody>
      </table>
    )
  }

}
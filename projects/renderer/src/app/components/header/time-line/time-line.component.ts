import { Component, OnInit } from '@angular/core'
import { fetchUpdateHistory } from './update-history'
import { UpdateHistoryByDate } from './update-history.interface'

@Component({
  selector: 'time-line',
  templateUrl: './time-line.component.html',
  styleUrls: ['./time-line.component.css'],
})
export class TimeLineComponent implements OnInit {
  updateHistory: UpdateHistoryByDate[] = []

  async ngOnInit(): Promise<void> {
    const historyBydate = await fetchUpdateHistory()
    this.updateHistory = historyBydate.map((history) => {
      return {
        date: history.key,
        history: history.value,
      }
    })
    console.log(this.updateHistory)
  }
}

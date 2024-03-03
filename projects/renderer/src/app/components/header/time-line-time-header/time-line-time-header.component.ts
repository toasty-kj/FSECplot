import { Component, Input } from '@angular/core'

@Component({
  selector: 'time-line-time-header',
  templateUrl: './time-line-time-header.component.html',
  styleUrls: ['./time-line-time-header.component.css'],
})
export class TimeLineTimeHeaderComponent {
  @Input() timeStr = ''
}

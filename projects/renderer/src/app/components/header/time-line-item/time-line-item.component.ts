import { Component, Input } from '@angular/core'

@Component({
  selector: 'time-line-item',
  templateUrl: './time-line-item.component.html',
  styleUrls: ['./time-line-item.component.css'],
})
export class TimeLineItemComponent {
  @Input() title = ''
  @Input() content = ''
  @Input() auther = ''
}

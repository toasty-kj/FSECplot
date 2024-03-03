import { Component, Input, OnChanges, SimpleChanges } from '@angular/core'

@Component({
  selector: 'form-title',
  templateUrl: './form-title.component.html',
  styleUrls: ['./form-title.component.css'],
})
export class FormTitleComponent {
  @Input() title = ''
  @Input() infoContent = ''
}

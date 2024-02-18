import { Component, EventEmitter, Input, Output } from '@angular/core'

@Component({
  selector: 'dropdown-form',
  templateUrl: './dropdown-form.component.html',
  styleUrls: ['./dropdown-form.component.css'],
})
export class DropdownFormComponent {
  @Input() title: string = ''
  @Input() label: string = ''
  @Output() tags = new EventEmitter<string>()

  changeInputTag(event: any) {
    const value = event.target.value
    this.tags.emit(value)
  }
}

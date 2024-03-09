import { Component, Input, OnChanges, SimpleChanges } from '@angular/core'
import { MessageService } from 'primeng/api'
import { toastType } from './toast-type'

@Component({
  selector: 'toast',
  templateUrl: './toast.component.html',
  providers: [MessageService],
  styleUrl: './toast.component.css',
})
export class ToastComponent implements OnChanges {
  constructor(private messageService: MessageService) {}
  @Input() severity = toastType.NotDefined
  @Input() detail = ''
  toastType = toastType

  // 入力された内容が変更されたらtoastificationを表示する
  ngOnChanges(changes: SimpleChanges) {
    if (!changes['detail']) return
    const messageChange = changes['detail']
    // 初期化の際は2秒待ってから表示する
    if (messageChange.previousValue === undefined) {
      setTimeout(() => {
        this.show()
      }, 1000)
    } else {
      this.show()
    }
  }

  show() {
    this.messageService.add({
      severity: this.severity,
      detail: this.detail,
    })
  }

  clear() {
    this.messageService.clear()
  }
}

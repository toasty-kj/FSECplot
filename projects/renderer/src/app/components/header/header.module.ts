import { NgModule } from '@angular/core'
import { CommonModule } from '@angular/common'
import { HeaderComponent } from './header/header.component'
import { TimeLineComponent } from './time-line/time-line.component'
import { TimeLineItemComponent } from './time-line-item/time-line-item.component'
import { TimeLineTimeHeaderComponent } from './time-line-time-header/time-line-time-header.component'

@NgModule({
  declarations: [
    HeaderComponent,
    TimeLineComponent,
    TimeLineItemComponent,
    TimeLineTimeHeaderComponent,
  ],
  imports: [CommonModule],
  exports: [HeaderComponent],
})
export class HeaderModule {}

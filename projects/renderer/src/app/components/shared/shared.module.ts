import { NgModule } from '@angular/core'
import { CommonModule } from '@angular/common'
import { TooltipInfoComponent } from './tooltip-info/tooltip-info.component'

@NgModule({
  declarations: [TooltipInfoComponent],
  imports: [CommonModule],
  exports: [TooltipInfoComponent],
})
export class SharedModule {}

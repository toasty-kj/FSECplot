import { NgModule } from '@angular/core'
import { CommonModule } from '@angular/common'
import { HomePageComponent } from './home-page/home-page.component'
import { InputFormModule } from '../../components/input-form/input-form.module'
import { ReactiveFormsModule } from '@angular/forms'

@NgModule({
  declarations: [HomePageComponent],
  imports: [CommonModule, InputFormModule, ReactiveFormsModule],
  exports: [HomePageComponent],
})
export class HomePageModule {}

import { NgModule } from '@angular/core'
import { CommonModule } from '@angular/common'
import { HomePageComponent } from './home-page/home-page.component'
import { FileUploaderComponent } from './file-uploader/file-uploader.component'

@NgModule({
  declarations: [HomePageComponent, FileUploaderComponent],
  imports: [CommonModule],
  exports: [HomePageComponent],
})
export class HomePageModule {}

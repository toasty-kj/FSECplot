import { NgModule } from '@angular/core'
import { CommonModule } from '@angular/common'
import { FileUploaderComponent } from './file-uploader/file-uploader.component'
import { DropdownFormComponent } from './dropdown-form/dropdown-form.component'
import { InputFormComponent } from './input-form/input-form.component'

@NgModule({
  declarations: [
    FileUploaderComponent,
    DropdownFormComponent,
    InputFormComponent,
  ],
  imports: [CommonModule],
  exports: [FileUploaderComponent, DropdownFormComponent, InputFormComponent],
})
export class InputFormModule {}

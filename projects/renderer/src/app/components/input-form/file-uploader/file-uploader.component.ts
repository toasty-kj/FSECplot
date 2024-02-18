import { Component, EventEmitter, OnInit, Output } from '@angular/core'
import { SendDataService } from '../../../service/send-data.service'

@Component({
  selector: 'app-file-uploader',
  templateUrl: './file-uploader.component.html',
  styleUrls: ['./file-uploader.component.css'],
})
export class FileUploaderComponent {
  @Output() filePathList = new EventEmitter<string[]>()

  /**ファイルが選択された際に選択されたファイルパスを取得する */
  async onFileSelected(event: any) {
    const files: File = event.target.files
    const filePathList = this.getFilePathListFromFileList(files)
    this.filePathList.emit(filePathList)
    // const response = await this.api.sendSelectedFilePathList(filePathList)
    // console.log(JSON.stringify(response))
  }

  getFilePathListFromFileList = (fileList: any) => {
    const filePathList: string[] = []
    for (let i = 0; i < fileList.length; i++) {
      filePathList.push(fileList[i.toString()].path)
    }
    return filePathList
  }
}

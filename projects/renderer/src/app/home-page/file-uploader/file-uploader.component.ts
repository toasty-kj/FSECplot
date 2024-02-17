import { Component, OnInit } from '@angular/core'
import { HttpClient, HttpParams } from '@angular/common/http'
import { SendDataService } from '../../send-data.service'

@Component({
  selector: 'app-file-uploader',
  templateUrl: './file-uploader.component.html',
  styleUrls: ['./file-uploader.component.css'],
})
export class FileUploaderComponent implements OnInit {
  users: { userId: number; userName: string }[] = []
  currentTime = new Date()

  URL = 'http://127.0.0.1:5000/api'

  constructor(private api: SendDataService) {}

  async ngOnInit() {}

  /**ファイルが選択された際に選択されたファイルパスを取得する */
  async onFileSelected(event: any) {
    const files: File = event.target.files
    const filePathList = this.getFilePathListFromFileList(files)
    console.log(filePathList)

    const response = await this.api.sendSelectedFilePathList(filePathList)
    console.log(JSON.stringify(response))
  }

  getFilePathListFromFileList = (fileList: any) => {
    const filePathList: string[] = []
    for (let i = 0; i < fileList.length; i++) {
      filePathList.push(fileList[i.toString()].path)
    }
    return filePathList
  }
}

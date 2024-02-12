import { Component, OnInit } from '@angular/core'

@Component({
  selector: 'app-file-uploader',
  templateUrl: './file-uploader.component.html',
  styleUrls: ['./file-uploader.component.css'],
})
export class FileUploaderComponent implements OnInit {
  users: { userId: number; userName: string }[] = []
  currentTime = new Date()

  async ngOnInit() {
    this.users = await window.myAPI.loadUsers()
  }

  /**ファイルが選択された際に選択されたファイルパスを取得する */
  onFileSelected(event: any) {
    const files: File = event.target.files
    const filePathList = this.getFilePathListFromFileList(files)
    console.log(filePathList)
  }

  getFilePathListFromFileList = (fileList: any) => {
    const filePathList: string[] = []
    for (let i = 0; i < fileList.length; i++) {
      filePathList.push(fileList[i.toString()].path)
    }
    return filePathList
  }
}

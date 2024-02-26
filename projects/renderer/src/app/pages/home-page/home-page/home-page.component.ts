import { Component } from '@angular/core'
import { SendDataService } from '../../../service/send-data.service'
import { logoBase64 } from './logo-image'

@Component({
  selector: 'app-home-page',
  templateUrl: './home-page.component.html',
  styleUrls: ['./home-page.component.css'],
})
export class HomePageComponent {
  logoImage = logoBase64
  tag = ''
  title = ''
  filePath: string[] = []
  constructor(private api: SendDataService) {}

  getTag(newTag: string) {
    this.tag = newTag
  }

  getInputTitle(newTitle: string) {
    this.title = newTitle
  }

  async getFilePath(newFilePath: string[]) {
    this.filePath = newFilePath
    // filepathからデフォルトのデータ名をバックエンドから取得する
    const result = await this.api.getDefaultNameByFilePathList(this.filePath)
    console.log(result)
  }

  async _onSubmit() {
    // TODO 入力のバリデーションを作成する
    const responce = await this.api.sendSelectedFilePathList(
      this.filePath,
      this.title,
      this.tag,
    )
    console.log(responce)
  }
}

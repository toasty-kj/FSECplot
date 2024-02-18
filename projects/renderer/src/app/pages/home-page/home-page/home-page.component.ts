import { Component } from '@angular/core'
import { app } from 'electron'
import { SendDataService } from '../../../service/send-data.service'

@Component({
  selector: 'app-home-page',
  templateUrl: './home-page.component.html',
  styleUrls: ['./home-page.component.css'],
})
export class HomePageComponent {
  tag = ''
  title = ''
  filePath: string[] = []
  constructor(private api: SendDataService) {}

  getTag(newTag: string) {
    this.tag = newTag
  }

  getInputTitle(newTitle: string) {
    this.title = newTitle
    console.log(this.title)
  }

  getFilePath(newFilePath: string[]) {
    this.filePath = newFilePath
    console.log(this.filePath)
  }

  async _onSubmit() {
    console.log('on click!!', this.filePath, this.title, this.tag)
    // TODO 入力のバリデーションを作成する
    const responce = await this.api.sendSelectedFilePathList(
      this.filePath,
      this.title,
      this.tag,
    )
    console.log(responce)
  }
}

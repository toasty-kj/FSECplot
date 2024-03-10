import { Component, OnChanges, SimpleChanges } from '@angular/core'
import { MessageService } from 'primeng/api'
import { SendDataService } from '../../../service/send-data.service'
import { logoBase64 } from './logo-image'
import { FormArray, FormBuilder, FormGroup, Validators } from '@angular/forms'
import {
  ToastContent,
  toastType,
} from '../../../components/shared/toast/toast-type'
@Component({
  selector: 'app-home-page',
  templateUrl: './home-page.component.html',
  providers: [MessageService],
  styleUrls: ['./home-page.component.css'],
})
export class HomePageComponent {
  logoImage = logoBase64
  tag = ''
  title = ''
  filePath: string[] = []
  pathAndDefaultName: { path: string; name: string }[] = []
  dataNameList: FormGroup
  currentVersion = ''
  toastContent: ToastContent = { type: toastType.NotDefined, message: '' }
  isDownloading = false

  constructor(
    private api: SendDataService,
    private fb: FormBuilder,
  ) {
    this.dataNameList = this.fb.group({
      dataArray: this.fb.array([]),
    })
    this.getCurrentVersion()
    this.getDownloadingStatus()
  }

  /** 現在のバージョンを取得する */
  async getCurrentVersion() {
    this.currentVersion = await window.api.getVersion()
    // 金曜日は表示メッセージを変更する
    const dayOfWeek = this.getDayOfWeek()
    const message =
      dayOfWeek == 5
        ? 'Happy Friday🎉'
        : `you are using version ${this.currentVersion}`
    this.createToast(toastType.Success, message)
  }

  /**
   *  本日の曜日を取得する
   *  // 0: 日曜日, 1: 月曜日, ..., 6: 土曜日
   *  */
  getDayOfWeek() {
    const date = new Date()
    const jstDate = new Date(date.getTime() + 9 * 60 * 60 * 1000)
    return jstDate.getDay()
  }

  /** ダウンロードのステータスを取得する */
  async getDownloadingStatus() {
    // 5秒おきにダウンロードのステータスをmainに確認する
    setInterval(async () => {
      const previousStatus = this.isDownloading
      this.isDownloading = await window.api.getDownloadingStatus()
      if (previousStatus == true && this.isDownloading == false) {
        this.createToast(toastType.Success, 'downdload finished')
      }
      console.log(this.isDownloading)
    }, 5000)
  }

  getTag(newTag: string) {
    this.tag = newTag
  }

  getInputTitle(newTitle: string) {
    this.title = newTitle
  }

  async getFilePath(newFilePath: string[]) {
    this.filePath = newFilePath
    // filepathからデフォルトのデータ名をバックエンドから取得する
    this.pathAndDefaultName = await this.api.getDefaultNameByFilePathList(
      this.filePath,
    )
    this.initFormArray()
  }

  async _onSubmit() {
    const isError = this.validateOnSubmit()
    if (isError) return

    const responce = await this.api.sendSelectedFilePathList(
      this.filePath,
      this.dataArray.value,
      this.title,
      this.tag,
    )
    console.log(responce)
  }

  validateOnSubmit() {
    let isError = false
    if (this.filePath.length == 0) {
      this.createToast(toastType.Error, 'Please input files')
      isError = true
    }

    if (this.title == '') {
      this.createToast(toastType.Error, 'Please input title')
      isError = true
    }

    if (this.tag == '') {
      this.createToast(
        toastType.Error,
        'Please select fluorescence type for plotting',
      )
      isError = true
    }
    return isError
  }

  initFormArray() {
    // フォームグループを初期化する
    this.dataNameList = this.fb.group({
      dataArray: this.fb.array([], Validators.required),
    })

    // 選択されたファイルの数だけフォームを作成する
    this.pathAndDefaultName.forEach((element) => {
      ;(this.dataNameList.get('dataArray') as FormArray).push(
        this.fb.control(element.name),
      )
    })
  }

  get dataArray(): FormArray {
    return this.dataNameList.get('dataArray') as FormArray
  }

  /** トーストに値を設定する */
  createToast(type: toastType, message: string) {
    this.toastContent = {
      type: type,
      message: message,
    }
  }
}

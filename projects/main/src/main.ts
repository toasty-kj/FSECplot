import { app, BrowserWindow, autoUpdater, dialog } from 'electron'
import * as path from 'path'
import * as fs from 'fs'
import debug from 'electron-debug'
import electronReloader from 'electron-reloader'
import { PythonShell } from 'python-shell'
import { spawn } from 'child_process'

//Windowsにインストールした時用の処理
//参考URL:https://www.electronforge.io/config/makers/squirrel.windows
if (require('electron-squirrel-startup')) app.quit()

//自動アップデートに対応
require('update-electron-app')()

function createWindow() {
  const isDevMode: boolean = !!process.argv.find(
    (val) => val === '--development',
  )

  const win = new BrowserWindow({
    height: 600,
    webPreferences: {
      preload: path.join(__dirname, 'preload.js'),
    },
    width: 800,
    //icon: path.join(__dirname, 'assets/icon/icon.ico'),
    icon: path.join(__dirname, '../assets/icon/icon.ico'),
  })

  if (isDevMode) {
    //開発モード
    //electron-debugツールを実行する。
    debug()

    try {
      //electron-reloaderを実行する。
      electronReloader(module, {
        watchRenderer: false, //レンダラー側の変更は監視しない。
      })
    } catch {}

    win.loadURL('http://localhost:4200')

    //開発ツールを開く。
    win.webContents.openDevTools()
  } else {
    //本番モード
    win.loadFile(path.join(__dirname, 'renderer/index.html'))
  }
  return win
}

app.whenReady().then(async () => {
  if (require('electron-squirrel-startup')) {
    console.log(`app.quit実行`)
    app.quit()
  }

  // パッケージ化する際には読み込むpythonファイルのパスを変更する
  // exe: リリースの際は下記コメントアウトとsubpy.kill()を有効化する 'main/main'
  const subpy = require('child_process').spawn(
    path.join(__dirname, 'main/main'),
  )

  // dev: 開発の場合は下記コメントアウトを有効化する 'projects/main/src/main.py'
  // PythonShell.run('projects/main/src/main.py')
  //   .then((res) => {
  //     fs.writeFileSync('python-shell.log', res.toString())
  //   })
  //   .catch((err) => {
  //     fs.writeFileSync('python-shell-error.log', err.toString())
  //   })

  createWindow()

  app.on('activate', function () {
    if (BrowserWindow.getAllWindows().length === 0) createWindow()
  })

  app.on('window-all-closed', () => {
    if (process.platform !== 'darwin') {
      // TODO リリースの際には有効化する
      subpy.kill()
      app.quit()
    }
  })
})

// ファイルの末尾に追加
const server = 'https://update.electronjs.org'
const feed = `${server}/toasty-kj/FSECplot/${process.platform}-${process.arch}/${app.getVersion()}`
fs.writeFileSync('python-shell.log', feed)
console.log(feed)

if (app.isPackaged) {
  // パッケージされている（ローカル実行ではない）
  autoUpdater.setFeedURL({
    url: feed,
  })
  autoUpdater.checkForUpdates() // アップデートを確認する

  // アップデートのダウンロードが完了したとき
  autoUpdater.on('update-downloaded', async () => {
    const returnValue = await dialog.showMessageBox({
      message: 'アップデートあり',
      detail: '再起動してインストールできます。',
      buttons: ['再起動', '後で'],
    })
    if (returnValue.response === 0) {
      autoUpdater.quitAndInstall() // アプリを終了してインストール
    }
  })

  // アップデートがあるとき
  autoUpdater.on('update-available', () => {
    dialog.showMessageBox({
      message: 'アップデートがあります',
      detail: 'ダウンロード完了後に再度通知されます。',
      buttons: ['OK'],
    })
    // TODO ダウンロードフラグを立てて、update完了したらフラグを折る。フラグが立っている間は画面はローディング画面を表示する
  })

  // アップデートがないとき
  autoUpdater.on('update-not-available', () => {
    dialog.showMessageBox({
      message: 'アップデートはありません',
      buttons: ['OK'],
    })
  })

  // エラーが発生したとき
  autoUpdater.on('error', () => {
    dialog.showMessageBox({
      message: 'アップデートエラーが起きました',
      buttons: ['OK'],
    })
  })
}

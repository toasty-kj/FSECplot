import { groupByKey } from '../../shared/utility-function/groupObjectListByKey'
import { UpdateHistory, UpdateHistoryByDate } from './update-history.interface'

/** 更新履歴を読み込んで日付ごとにまとめて返す */
export async function fetchUpdateHistory() {
  // 更新履歴のファイルを読み込む
  const updateHistory =
    (await window.api.readUpdateHistory()) as unknown as UpdateHistory[]

  // date毎に更新履歴をまとめる
  return groupByKey(updateHistory, 'date')
}

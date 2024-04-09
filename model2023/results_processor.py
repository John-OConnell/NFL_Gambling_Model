
from sklearn.metrics import mean_squared_error

def calc_winning_percentage(results):
    win_count, no_bet = 0, 0
    for index in results.index:
            # get data from each column
            ht_pts_diff = results['ht_pts_diff'][index]
            vegas_line = results['ht_vegas_line'][index]
            model_pred = round(results['model_pred'][index])

            # model predicts ht victory, vegas predicts ht victory or pick em
            if model_pred > 0 and vegas_line <= 0:
                # model predicts larger margin of victory than vegas and ht covers
                if model_pred > abs(vegas_line) and ht_pts_diff > abs(vegas_line):
                    print("Vegas Line: ", vegas_line, ", model pred: ", -(model_pred), ", final pts diff: ", ht_pts_diff)
                    win_count+=1
                # model predicts smaller margin of victory than vegas and at covers
                elif model_pred < abs(vegas_line) and ht_pts_diff < abs(vegas_line):
                    print("Vegas Line: ", vegas_line, ", model pred: ", -(model_pred), ", final pts diff: ", ht_pts_diff)
                    win_count+=1
                # model prediction same as vegas - no bet
                elif model_pred == abs(vegas_line):
                    no_bet+=1
            # model predicts ht victory, vegas predicts ht loss
            elif model_pred > 0 and vegas_line > 0:
                # ht wins or covers
                if ht_pts_diff > 0 or abs(ht_pts_diff) < vegas_line:
                    print("Vegas Line: ", vegas_line, ", model pred: ", -(model_pred), ", final pts diff: ", ht_pts_diff)
                    win_count+=1
            # model predicts ht loss, vegas predicts ht loss or pick em
            elif model_pred < 0 and vegas_line >= 0:
                # model predicts smaller margin of loss than vegas and ht wins or covers
                if abs(model_pred) < vegas_line and (ht_pts_diff > 0 or abs(ht_pts_diff) < vegas_line):
                    print("Vegas Line: ", vegas_line, ", model pred: ", -(model_pred), ", final pts diff: ", ht_pts_diff)
                    win_count+=1
                # model predicts larger margin of loss than vegas and at covers
                elif abs(model_pred) > vegas_line and ht_pts_diff < 0 and abs(ht_pts_diff) > vegas_line:
                    print("Vegas Line: ", vegas_line, ", model pred: ", -(model_pred), ", final pts diff: ", ht_pts_diff)
                    win_count+=1
                # model predicts same as vegas - no bet
                elif abs(model_pred) == vegas_line:
                    no_bet+=1
            # model predicts ht loss, vegas predicts ht win
            elif model_pred < 0 and vegas_line < 0:
                # at wins or covers
                if ht_pts_diff < 0 or ht_pts_diff < abs(vegas_line):
                    print("Vegas Line: ", vegas_line, ", model pred: ", -(model_pred), ", final pts diff: ", ht_pts_diff)
                    win_count+=1
            # model precits pick em
            elif model_pred == 0:
                # vegas predicts ht loss and ht wins or covers
                if vegas_line > 0 and (ht_pts_diff > 0 or abs(ht_pts_diff) < vegas_line):
                    print("Vegas Line: ", vegas_line, ", model pred: ", -(model_pred), ", final pts diff: ", ht_pts_diff)
                    win_count+=1
                # vegas predicts at loss and at wins or covers
                if vegas_line < 0 and (ht_pts_diff < 0 or ht_pts_diff < abs(vegas_line)):
                    print("Vegas Line: ", vegas_line, ", model pred: ", -(model_pred), ", final pts diff: ", ht_pts_diff)
                    win_count+=1
            # check to make sure everything is accounted for
            else:
                print('something not accounted for')
                print(ht_pts_diff, vegas_line, model_pred)
                
    print(f'Total Number of Games:\n {len(results.index)}')
    print(f'Winning Bets Count:\n {win_count}')
    print(f'No Bet Placed Count:\n {no_bet}')
    print(f'Winning Percentage:\n {win_count /(len(results.index) - no_bet):.4f}')

def calc_classification_percentage(results):
    count = 0
    # loop through results df
    for index in results.index:
        ht_pts_diff = results['ht_pts_diff'][index]
        model_pred = results['model_pred'][index]
        # the model predicted a home team win and the home team won
        if model_pred > 0 and ht_pts_diff > 0:
            count+=1
        # the model predicted a home team loss and the home team lost
        elif model_pred < 0 and ht_pts_diff < 0:
            count+=1
            
    print(f'Winner Correctly Predicted Count:\n {count}')
    print(f'Accuracy in Classifaction:\n {count/len(results.index):.4f}')

def calc_mse_rmse(results):
    # calculating the mse and rmse of the data
    mse = mean_squared_error(results['ht_pts_diff'], results['model_pred'])
    rmse = mean_squared_error(results['ht_pts_diff'], results['model_pred'], squared = False)

    print(f'Mean Squared Error of Results:\n {mse:.4f}')
    print(f'Root Mean Squared Error of Results:\n {rmse:.4f}')

def process_results(results):

    calc_winning_percentage(results)
    print('______________________________________')
    calc_classification_percentage(results)
    print('______________________________________')
    calc_mse_rmse(results)
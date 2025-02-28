"""
Default parameters for training.

"""
# cfg_mk = {
#     'diff_area_noise': False,
#     'area': 3,
#     'gamma_rec': True, # True if recurrent distribution for Crec is gamma
#     'path': '/Users/michael/Documents/GitHub/multi-area/'
# }

defaults = {
    'extra_info': {},
    'Nin': 0,
    'N': 100,
    'Nout': 1,
    'rectify_inputs': False,
    'train_brec': False,
    'brec': 0,
    'train_bout': False,
    'bout': 0,
    'train_x0': True,
    'x0': 0.1,
    'mode': 'batch',
    'tau': 100,
    'tau_in': 100,
    'Cin': None,
    'Crec': None,
    'Cout': None,
    'ei': None,
    'ei_out': None,  # JCK ADDED THIS 2016-12-16
    'ei_positive_func': 'rectify',
    'hidden_activation': 'rectify',
    'output_activation': 'linear',
    'n_gradient': 20,
    'n_validation': 1000,
    'gradient_batch_size': None,
    'validation_batch_size': None,
    'lambda_Omega': 2,
    'lambda1_in': 0,
    'lambda1_rec': 0,
    'lambda1_out': 0,
    'lambda2_in': 0,
    'lambda2_rec': 0,
    'lambda2_out': 0,
    'lambda2_r': 0,
    'callback': None,
    'performance': None,
    'terminate': (lambda performance_history: False),
    'min_error': 0,
    'learning_rate': 1e-2,
    'max_gradient_norm': 1,
    'bound': 1e-20,
    'baseline_in': 0.2,
    'var_in': 0.01**2,
    'var_rec': 0.15**2,
    'seed': 1234,
    'gradient_seed': 11,
    'validation_seed': 22,
    'structure': {},
    'rho0': 1.5,
    'max_iter': int(1e7),
    'dt': None,
    'distribution_in': None,
    'distribution_rec': None,
    'distribution_out': None,
    'gamma_k': 2,
    'checkfreq': None,
    'patience': None,
    'momentum': False,  # Not used currently
    'method': 'sgd'  # Not used currently
}


def generate_trial(rng, dt, params):
    """
    Recommended structure for the `generate_trial` function.

    """
    pass
